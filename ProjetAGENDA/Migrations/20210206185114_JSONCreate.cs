using Microsoft.EntityFrameworkCore.Migrations;

namespace ProjetAGENDA.Migrations
{
    public partial class JSONCreate : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "jsonName",
                table: "AspNetUsers",
                nullable: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "jsonName",
                table: "AspNetUsers");
        }
    }
}
